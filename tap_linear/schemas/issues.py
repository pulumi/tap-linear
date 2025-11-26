from singer_sdk import typing as th

issuesSchema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("title", th.StringType),
    th.Property("url", th.StringType),
    th.Property("updatedAt", th.DateTimeType),
    th.Property("dueDate", th.DateType),
    th.Property(
        "state",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("type", th.StringType),
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
        "project",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        ),
    ),
    th.Property(
        "team",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        ),
    ),
).to_dict()
