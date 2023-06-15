#
# Clear headers from unparseble comments in code
# Author: info@rickvanderzwet.nl
# License: BSD
#
import click
import pathlib
import logging

logger = logging.getLogger(__name__)

def commit_warning(commit):
    if not commit:
        logger.warning("Dry-run, apply changes using --commit flag")


@click.command()
@click.argument('basedir', type=click.Path(exists=True, path_type=pathlib.Path, file_okay=False))
@click.option('--commit/--no-commit', default=False)
def strip_woo_header(basedir, commit):
    commit_warning(commit)
    """ Strip header bit of files up-to special BOM marker"""
    marker = '\ufeff'.encode('utf-8')

    for p in basedir.glob('**/*'):
        if not p.is_file():
            continue

        content = p.open('rb').read()
        if marker in content:
            logger.info("Converting '%s'", p)
            if commit:
                p.open('wb').write(content.split(marker)[1])
    commit_warning(commit)


if __name__ == '__main__':
    logging.basicConfig(format='# %(levelname).4s: %(message)s', level=logging.DEBUG)
    strip_woo_header()
