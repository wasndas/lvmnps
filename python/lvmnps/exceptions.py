# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2017-12-05 12:01:21
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2017-12-05 12:19:32

from __future__ import absolute_import, division, print_function


class NpsActorError(Exception):
    """A custom core NpsActor exception"""

    def __init__(self, message=None):

        message = "There has been an error" if not message else message

        super(NpsActorError, self).__init__(message)


class NpsActorNotImplemented(NpsActorError):
    """A custom exception for not yet implemented features."""

    def __init__(self, message=None):

        message = "This feature is not implemented yet." if not message else message

        super(NpsActorNotImplemented, self).__init__(message)


class NpsActorAPIError(NpsActorError):
    """A custom exception for API errors"""

    def __init__(self, message=None):
        if not message:
            message = "Error with Http Response from NpsActor API"
        else:
            message = "Http response error from NpsActor API. {0}".format(message)

        super(NpsActorAPIError, self).__init__(message)


class NpsActorApiAuthError(NpsActorAPIError):
    """A custom exception for API authentication errors"""

    pass


class NpsActorMissingDependency(NpsActorError):
    """A custom exception for missing dependencies."""

    pass


class NpsActorWarning(Warning):
    """Base warning for NpsActor."""


class NpsActorUserWarning(UserWarning, NpsActorWarning):
    """The primary warning class."""

    pass


class NpsActorSkippedTestWarning(NpsActorUserWarning):
    """A warning for when a test is skipped."""

    pass


class NpsActorDeprecationWarning(NpsActorUserWarning):
    """A warning for deprecated features."""

    pass
