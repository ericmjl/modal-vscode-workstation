import modal

# Define the Modal image with necessary packages
image = (
    modal.Image.debian_slim()
    .apt_install("git", "wget", "ca-certificates", "gpg")
    .run_commands(
        """wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg && \
        install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg && \
        echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | tee /etc/apt/sources.list.d/vscode.list > /dev/null && \
        rm -f packages.microsoft.gpg"""
    )
    .apt_install("apt-transport-https")
    .apt_install("code")
    .apt_install("curl")
    .run_commands("""curl -fsSL https://pixi.sh/install.sh | sh""")
    .env({"PATH": "/root/.pixi/bin:$PATH"})
)

dot_vscode_volume = modal.Volume.from_name("vscode-server", create_if_missing=True)
dot_vscode_server_volume = modal.Volume.from_name(
    "vscode-server-dir", create_if_missing=True
)
repo_volume = modal.Volume.from_name("workstation-code-dir", create_if_missing=True)

# Deploy the function as a web endpoint
app = modal.App("vscode-server")


@app.function(
    image=image,
    volumes={
        "/root/.vscode": dot_vscode_volume,
        "/root/.vscode-server": dot_vscode_server_volume,
        "/root/_repos": repo_volume,
    },
)
def run_vscode_server():
    import subprocess

    subprocess.Popen(
        "code tunnel",
        shell=True,
    )
    while True:
        pass
