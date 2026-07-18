from huggingface_hub import hf_hub_download


def download_artifact(repo_id: str, filename: str):
    """
    Download a file from Hugging Face Hub.

    Parameters
    ----------
    repo_id : str
        Example:
        "your_username/employee-attrition-model"

    filename : str
        Example:
        "model.pkl"

    Returns
    -------
    str
        Local cached file path.
    """

    return hf_hub_download(
        repo_id=repo_id,
        filename=filename,
    )