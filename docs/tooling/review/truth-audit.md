---
page_type: reference
---

# Proof Audit

## Source identity

- Source repository: `qualcomm-linux/meta-qcom`
- Proof fork: `justinr1234/meta-qcom-docs-proof`
- Source snapshot: `8ec7db3048b716651a027924402f90626b3aca51`
- Source branch: `master`

## Scope

The reviewed source units are `conf/layer.conf` and
`recipes-bsp/partition/mount-tee-partition/check-tee-partition-fs.sh`.
Generated output, CI fixtures, patches, licenses, and vendor or build
artifacts are excluded from inline authoring.

## Truth and preservation checks

- The layer settings in `conf/layer.conf` match the values rendered in the
  layer reference page.
- The shell header matches the script's device check, filesystem probe,
  read-only check, and recreation branches.
- Existing shell copyright, SPDX, and operational comments remain unchanged.
- Every page in the route manifest is linked from the landing-page toctree.
- The source repository was cloned read-only and received no commits or
  branches.
