class ErrorType:
    BAD_REQUEST = 'BAD_REQUEST'
    FORBIDDEN = 'FORBIDDEN'
    UNSUPPORTED = 'UNSUPPORTED'
    INTERNAL_ERROR = 'INTERNAL_ERROR'


class ErrorSubType:
    # BAD_REQUEST
    BAD_VERSION = 'BAD_VERSION'
    BAD_TYPE = 'BAD_TYPE'
    BAD_GRAPH = 'BAD_GRAPH'
    BAD_BLOCK = 'BAD_BLOCK'
    BAD_CONNECTOR = 'BAD_CONNECTOR'
    BAD_HEADER_MATCH = 'BAD_HEADER_MATCH'
    BAD_PAYLOAD_MATCH = 'BAD_PAYLOAD_MATCH'
    BAD_FILE = 'BAD_FILE'
    ILLEGAL_ARGUMENT = 'ILLEGAL_ARGUMENT'
    ILLEGAL_STATE = 'ILLEGAL_STATE'

    #FORBIDDEN
    NOT_PERMITTED = 'NOT_PERMITTED'
    NO_ACCESS = 'NO_ACCESS'

    # UNSUPPORTED
    UNSUPPORTED_VERSION = 'UNSUPPORTED_VERSION'
    UNSUPPORTED_BLOCK = 'UNSUPPORTED_BLOCK'
    UNSUPPORTED_MESSAGE = 'UNSUPPORTED_MESSAGE'
    UNSUPPORTED_OTHER = 'UNSUPPORTED_OTHER'

    # INTERNAL
    ADD_MODULE_FAILED = 'ADD_MODULE_FAILED'
    INTERNAL_ERROR = 'INTERNAL_ERROR'


def exception_to_error_args(exception):
    # TODO: add real exception handling
    return ErrorType.INTERNAL_ERROR, ErrorSubType.INTERNAL_ERROR, exception.message, ''