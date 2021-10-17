from __future__ import annotations

from typing import ClassVar, List, Optional

from pydantic import AnyHttpUrl, BaseModel, Field, validator

from ..shared.validators import validate_semver


class AddonProperties(
    BaseModel, title="Add-on properties, as managed by Anki Add-on Builder"
):
    json_name: ClassVar[str] = "addon"  # json file name stem

    display_name: str = Field(
        ..., description="The name displayed in Anki's UI (e.g. in the add-on list)"
    )
    module_name: str = Field(
        ...,
        description=(
            "The module/package the add-on is imported as, i.e. the name of the add-on"
            " folder."
        ),
    )
    repo_name: str = Field(
        ...,
        description=(
            "The name of the git repository the add-on is hosted in. Currently only"
            " used for build names."
        ),
    )
    local_name_suffix: Optional[str] = Field(
        default=None,
        description=(
            "A suffix to the display name to apply when creating builds for non-ankiweb"
            " distribution."
        ),
        min_length=1
    )
    ankiweb_id: Optional[str] = Field(
        default=None, description="The AnkiWeb upload ID."
    )
    version: Optional[str] = Field(
        default=None,
        description=(
            "Add-on version string. Needs to follow semantic versioning guidelines."
        ),
    )
    author: str = Field(
        ..., description="The main author/maintainer/publisher of the add-on."
    )
    contact: Optional[str] = Field(
        default=None,
        description=(
            "Contact details to list for the author (e.g. either a website or email)"
        ),
    )
    homepage: Optional[AnyHttpUrl] = Field(
        default=None,
        description="Homepage of the add-on project (e.g. GitHub repository link)",
    )
    tags: Optional[str] = Field(
        default=None,
        description=(
            "Space-delimited list of tags that characterize the add-on on AnkiWeb."
        ),
    )
    copyright_start: Optional[int] = Field(
        default=None,
        description=(
            "Starting year to list for automatically generated copyright headers."
        ),
    )
    conflicts: Optional[List[str]] = Field(
        default=None,
        description=(
            "A list of other AnkiWeb add-on IDs or package names that conflict with"
            " this add-on."
        ),
        title="Conflicting Add-ons",
    )
    ankiweb_conflicts_with_local: Optional[bool] = Field(
        default=True, description="TODO"
    )
    local_conflicts_with_ankiweb: Optional[bool] = Field(
        default=True, description="TODO"
    )
    min_anki_version: Optional[str] = Field(
        default=None,
        description=(
            "SemVer version string describing the minimum required Anki version to run"
            " this add-on."
        ),
    )
    max_anki_version: Optional[str] = Field(
        default=None,
        description=(
            "SemVer version string describing the maximum supported Anki version of"
            " this add-on"
        ),
    )
    tested_anki_version: Optional[str] = Field(
        default=None,
        description=(
            "SemVer version string describing the latest Anki version this add-on was"
            " tested on."
        ),
    )

    _validate_versions = validator(
        "min_anki_version", "max_anki_version", "tested_anki_version", allow_reuse=True
    )(validate_semver)
