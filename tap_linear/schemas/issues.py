from singer_sdk import typing as th

issuesSchema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("identifier", th.StringType),
    th.Property("number", th.NumberType),
    th.Property("title", th.StringType),
    th.Property("description", th.StringType),
    th.Property("url", th.StringType),
    th.Property("branchName", th.StringType),
    th.Property("priority", th.NumberType),
    th.Property("priorityLabel", th.StringType),
    th.Property("estimate", th.NumberType),
    # TimelessDate scalar ("YYYY-MM-DD"), not a timestamp
    th.Property("dueDate", th.StringType),
    th.Property("trashed", th.BooleanType),
    th.Property("customerTicketCount", th.IntegerType),
    th.Property("createdAt", th.DateTimeType),
    th.Property("updatedAt", th.DateTimeType),
    th.Property("startedAt", th.DateTimeType),
    th.Property("completedAt", th.DateTimeType),
    th.Property("canceledAt", th.DateTimeType),
    th.Property("archivedAt", th.DateTimeType),
    th.Property("triagedAt", th.DateTimeType),
    th.Property("snoozedUntilAt", th.DateTimeType),
    th.Property(
        "state",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("type", th.StringType),
            th.Property("color", th.StringType),
            th.Property("position", th.NumberType),
        ),
    ),
    th.Property(
        "creator",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("email", th.StringType),
        ),
    ),
    th.Property(
        "assignee",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("email", th.StringType),
        ),
    ),
    th.Property(
        "parent",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("identifier", th.StringType),
            th.Property("title", th.StringType),
        ),
    ),
    th.Property(
        "project",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        ),
    ),
    th.Property(
        "projectMilestone",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("targetDate", th.StringType),
        ),
    ),
    th.Property(
        "team",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("key", th.StringType),
            th.Property("name", th.StringType),
        ),
    ),
    th.Property(
        "cycle",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("number", th.NumberType),
            th.Property("name", th.StringType),
            th.Property("startsAt", th.DateTimeType),
            th.Property("endsAt", th.DateTimeType),
        ),
    ),
    th.Property(
        "labels",
        th.ObjectType(
            th.Property(
                "nodes",
                th.ArrayType(
                    th.ObjectType(
                        th.Property("id", th.StringType),
                        th.Property("name", th.StringType),
                        th.Property("color", th.StringType),
                    )
                ),
            ),
        ),
    ),
    th.Property(
        "attachments",
        th.ObjectType(
            th.Property(
                "nodes",
                th.ArrayType(
                    th.ObjectType(
                        th.Property("id", th.StringType),
                        th.Property("url", th.StringType),
                        th.Property("title", th.StringType),
                        th.Property("subtitle", th.StringType),
                        th.Property("sourceType", th.StringType),
                        th.Property("source", th.ObjectType()),
                        th.Property("metadata", th.ObjectType()),
                        th.Property("createdAt", th.DateTimeType),
                    )
                ),
            ),
        ),
    ),
).to_dict()
