from pelican.readers import MarkdownReader
from pelican.utils import pelican_open
from pelican import signals

class MarkdownRawReader(MarkdownReader):
    """ 
    Extends MarkdownReader so that raw markdown is returned as a metadata property.
    This is useful for remark.js, where markdown will be parsed client-side. 
    """
    def read(self, source_path):
        content, metadata = super().read(source_path)
        with pelican_open(source_path) as raw:
            metadata['raw'] = raw
        return content, metadata

def add_reader(readers):
    readers.reader_classes['md'] = MarkdownRawReader

def register():
    signals.readers_init.connect(add_reader)

