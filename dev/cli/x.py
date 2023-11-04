import click

# TODO: Clean this all up.

def list_forks():
    print("list_forks")

def show_forks_status():
    print("show_forks_status")

def add_fork():
   print("list_forks")

def sync_fork():
    print("sync_fork")

# Groups

@click.group()
def cli():
    """🧪 Simple CLI to manage my OSS forks and experiments."""

@cli.group()
def forks():
    """Manage OSS forks."""

@cli.group()
def repos():
    """Manage owned repositories."""

@cli.group()
def templates():
    """Manage owned templates."""

@cli.group()
def projects():
    """Manage owned projects."""

@cli.group()
def wikis():
    """Manage owned wikis."""

# Commands

@forks.command()
def list():
    """List all my forked repositories."""
    list_forks()

@forks.command()
def status():
    """Get the status of the current forked repositories."""
    show_forks_status()

@forks.command()
def add():
    """Adds a new fork based on an existing source."""
    add_fork()
    
@forks.command()
def sync():
    """Syncs the fork with the latest upstream version."""
    sync_fork()
    
@forks.command()
def update():
    """Update the fork repository settings."""
    update_fork()

@forks.command()
def remove():
    """Remove the fork from acount."""
    remove_fork()
    
@forks.command()
def tag():
    """Tag the fork with a new version."""
    tag_fork()
    
@forks.command()
def publish():
    """Publish the fork to the registry."""
    publish_fork()
    
@forks.command()
def release():
    """Release the fork (tags & publishes the fork)."""
    release_fork()

@forks.command()
def contrib():
    """Contribute the fork changes back to upstream."""
    contrib_fork()
    
@repos.command()
def list():
    """List owning repository."""
    list_repos()
    
@repos.command()
def list():
    """Create owning repository."""
    create_repo()
    
@repos.command()
def create():
    """Create owning repository."""
    create_repo()
    
@repos.command()
def update():
    """Update owning repository."""
    update_repo()

@repos.command()
def remove():
    """Remove owning repository."""
    remove_repo()


if __name__ == '__main__':
    cli()
