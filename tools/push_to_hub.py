
from huggingface_hub import create_repo, upload_folder
from pathlib import Path

output_dir = "/home/ubuntu/4catalyzer-hackathon/opt/run-overnight/"

hub_token = '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'

repo_id = create_repo(
    repo_id=Path(output_dir).name, exist_ok=True, token=hub_token
).repo_id

print(repo_id)

upload_folder(
    repo_id=repo_id,
    folder_path=output_dir,
    commit_message="End of training",
    ignore_patterns=["step_*", "epoch_*"],
)