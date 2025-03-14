import wandb
import os

def init_wandb(LR=None, dataset=None, epochs=None):
    run_id = None

    # Check if there's a saved run ID
    if os.path.exists("wandb_run_id.txt"):
        with open("wandb_run_id.txt", "r") as f:
            run_id = f.read().strip()
    
    # If all params are None and a run ID exists, resume the existing run
    if LR is None and dataset is None and epochs is None and run_id:
        run = wandb.init(
            entity="claybattle-suny-binghamton",
            project="Bing Power Systems Study",
            id=run_id,
            resume="must"
        )
    else:
        # Start a new run
        run = wandb.init(
            entity="claybattle-suny-binghamton",
            project="Bing Power Systems Study",
            config={
                "learning_rate": LR,
                "architecture": "Existing",
                "dataset": dataset,
                "epochs": epochs,
            }
        )
        # Save run ID for future use
        with open("wandb_run_id.txt", "w") as f:
            f.write(run.id)

    return run

def end_wandb():
    """Ends the W&B run and deletes the saved run ID."""
    if os.path.exists("wandb_run_id.txt"):
        os.remove("wandb_run_id.txt")