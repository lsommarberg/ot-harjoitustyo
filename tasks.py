from invoke import task


@task
def start(ctx):
    ctx.run("src/main.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src/tests", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def coverage(ctx):
    ctx.run("coverage run -m pytest src/tests", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage report", pty=True)

@task(coverage)
def coverage_html(ctx):
    ctx.run("coverage html", pty=True)