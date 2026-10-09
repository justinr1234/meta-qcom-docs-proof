---
page_type: reference
---

# Persist Filesystem Check

`recipes-bsp/partition/mount-tee-partition/check-tee-partition-fs.sh` checks
`/dev/disk/by-partlabel/persist` before services use the persist partition.

Its behavior is intentionally narrow:

1. Exit successfully when the device node is absent.
2. Create an ext4 filesystem when `blkid` does not report ext4.
3. Run `e2fsck -n` for an existing ext4 filesystem.
4. Recreate the filesystem when the check returns an error greater than `4`.
5. Report that the filesystem is healthy for lower return codes.

The source keeps its original Qualcomm copyright, SPDX identifier, and
operational comments. The proof adds only the header describing the observed
control flow.
