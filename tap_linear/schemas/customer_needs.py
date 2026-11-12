from singer_sdk import typing as th

customerNeedsSchema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("createdAt", th.DateTimeType),
    th.Property("updatedAt", th.DateTimeType),
    th.Property("archivedAt", th.DateTimeType),
    th.Property("priority", th.NumberType),
    th.Property("body", th.StringType),
    th.Property("url", th.StringType),
    th.Property(
        "customer",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("externalIds", th.ArrayType(th.StringType)),
            th.Property("domains", th.ArrayType(th.StringType)),
            th.Property("revenue", th.IntegerType),
            th.Property("size", th.NumberType),
            th.Property(
                "tier",
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("name", th.StringType),
                ),
            ),
            th.Property(
                "status",
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("name", th.StringType),
                ),
            ),
        ),
    ),
    th.Property(
        "issue",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("identifier", th.StringType),
        ),
    ),
    th.Property(
        "originalIssue",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("identifier", th.StringType),
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
        "creator",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("email", th.StringType),
        ),
    ),
    th.Property(
        "attachment",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("url", th.StringType),
            th.Property("title", th.StringType),
            th.Property("sourceType", th.StringType),
            th.Property("source", th.ObjectType()),
            th.Property("metadata", th.ObjectType()),
        ),
    ),
).to_dict()
