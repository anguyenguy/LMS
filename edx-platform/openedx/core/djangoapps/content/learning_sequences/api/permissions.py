"""
Simple permissions for Learning Sequences.

Most access rules determining what a user will see are determined within the
outline processors themselves. This is where we'd put permissions that are used
to determine whether those processors even need to be run to filter the results.
"""
from opaque_keys.edx.keys import CourseKey

from lms.djangoapps.courseware.access import has_access
from openedx.core import types

from ..toggles import USE_FOR_OUTLINES


def can_call_public_api(course_key: CourseKey) -> bool:
    """
    This is only intended for rollout purposes, and eventually everyone will be
    able to call the public API for all courses.
    """
    return USE_FOR_OUTLINES.is_enabled(course_key)


def can_see_all_content(requesting_user: types.User, course_key: CourseKey) -> bool:
    """
    Global staff, course staff, and instructors can see everything.

    There's no need to run processors to restrict results for these users.
    """
    # has_access handles all possible staff cases, including checking for masquerading
    return has_access(requesting_user, 'staff', course_key).has_access
