import matplotlib.pyplot as plt
import numpy as np

def plot_simulation(sim: dict, save_path: str = None) -> None:
    p   = sim["params"]
    t   = sim["t"]
    z   = sim["z"]
    lam = sim["lam"]
    y   = sim["y"]

    fig, axes = plt.subplots(3, 1, figsize=(12, 9), sharex=True)
    fig.suptitle(
        rf"Poisson-AR(1):  $\mu={p['mu']}$,  $\phi={p['phi']}$,"
        rf"  $\sigma_\eta={p['sigma_eta']}$,  $n={p['n']}$",
        fontsize=13, fontweight="bold",
    )

    # latent log-intensity z_t 
    ax = axes[0]
    ax.plot(t, z, color="#2b6cb0", linewidth=1.2, label=r"$z_t$ (latent)")
    ax.axhline(p["mu"], color="#e53e3e", linewidth=1, linestyle="--",
               label=rf"$\mu = {p['mu']}$")
    sigma_stat = p["sigma_eta"] / np.sqrt(1 - p["phi"] ** 2)
    ax.fill_between(t,
                    p["mu"] - 2 * sigma_stat,
                    p["mu"] + 2 * sigma_stat,
                    alpha=0.12, color="#2b6cb0", label=r"$\mu \pm 2\,\sigma_\infty$")
    ax.set_ylabel(r"$z_t$")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, alpha=0.3)

    # time-varying intensity lambda_t = exp(z_t)
    ax = axes[1]
    ax.plot(t, lam, color="#d69e2e", linewidth=1.2, label=r"$\lambda_t = e^{z_t}$")
    ax.set_ylabel(r"$\lambda_t$")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, alpha=0.3)

    # observed counts y_t
    ax = axes[2]
    ax.bar(t, y, color="#276749", alpha=0.7, width=1.0, label=r"$y_t$ (counts)")
    ax.plot(t, lam, color="#d69e2e", linewidth=1.0, alpha=0.8,
            label=r"$\lambda_t$ (intensity)")
    ax.set_ylabel(r"$y_t$")
    ax.set_xlabel("Time $t$")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"  Plot saved → {save_path}")
    else:
        plt.show()