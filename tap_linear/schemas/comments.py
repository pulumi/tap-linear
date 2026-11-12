from singer_sdk import typing as th

commentsSchema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("createdAt", th.DateTimeType),
    th.Property("updatedAt", th.DateTimeType),
    th.Property("editedAt", th.DateTimeType),
    th.Property("archivedAt", th.DateTimeType),
    th.Property("body", th.StringType),
    th.Property("url", th.StringType),
    # Null for comments on project updates or documents.
    th.Property(
        "issue",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("identifier", th.StringType),
        ),
    ),
    # Set on thread replies.
    th.Property("parent", th.ObjectType(th.Property("id", th.StringType))),
    # A Linear user; null for comments synced from GitHub or Slack, which carry
    # externalUser, and for integration comments, which carry botActor.
    th.Property(
        "user",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("email", th.StringType),
        ),
    ),
    th.Property(
        "externalUser",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        ),
    ),
    th.Property(
        "botActor",
        th.ObjectType(
            th.Property("name", th.StringType),
            th.Property("type", th.StringType),
        ),
    ),
).to_dict()
