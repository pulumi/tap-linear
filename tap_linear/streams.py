"""Stream type classes for tap-linear."""

from tap_linear.client import LinearStream
from tap_linear.schemas.issues import issuesSchema
from tap_linear.queries.issues import issuesQuery
from tap_linear.schemas.customer_needs import customerNeedsSchema
from tap_linear.queries.customer_needs import customerNeedsQuery
from tap_linear.schemas.comments import commentsSchema
from tap_linear.queries.comments import commentsQuery


class IssuesStream(LinearStream):
    """Define custom stream."""

    name = "Issues"
    schema = issuesSchema
    primary_keys = ["id"]
    replication_key = "updatedAt"
    query = issuesQuery
    connection_field = "issues"


class CustomerNeedsStream(LinearStream):
    """Customer requests linking Linear customers to issues/projects."""

    name = "CustomerNeeds"
    schema = customerNeedsSchema
    primary_keys = ["id"]
    replication_key = "updatedAt"
    query = customerNeedsQuery
    connection_field = "customerNeeds"


class CommentsStream(LinearStream):
    """Comments on issues, project updates, and documents (threads included)."""

    name = "Comments"
    schema = commentsSchema
    primary_keys = ["id"]
    replication_key = "updatedAt"
    query = commentsQuery
    connection_field = "comments"
