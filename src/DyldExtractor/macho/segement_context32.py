from mmap import mmap
from typing import List, Dict


from DyldExtractor.macho.macho_structs import (
	segment_command,
	section
)


class SegmentContext(object):

	seg: segment_command

	sects: Dict[bytes, section]
	sectsI: List[section]

	def __init__(self, file: mmap, segment: segment_command) -> None:
		"""Represents a segment.

		This holds information regarding a segment and its sections.

		Args:
			file: The data source used for the segment.
			segment: The segment structure.
		"""

		super().__init__()

		self.seg = segment

		self.sects = {}
		self.sectsI = []

		sectsStart = segment._fileOff_ + len(segment)
		for i in range(segment.nsects):
			sectOff = sectsStart + (i * section.SIZE)
			sect = section(file, sectOff)

			self.sects[sect.sectname] = sect
