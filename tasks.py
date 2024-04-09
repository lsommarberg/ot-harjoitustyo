from invoke import task


@task
def start(ctx):
    ctx.run("src/main.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src/tests", pty=True)


@task
def coverage_report(ctx):
    ctx.run("coverage run -m pytest src/tests", pty=True)
    ctx.run("coverage report", pty=True)
    ctx.run("coverage html", pty=True)