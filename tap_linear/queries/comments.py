commentsQuery = """
query Comments($next: String, $replicationKeyValue: DateTimeOrDuration) {
    comments(
        first: 100
        after: $next
        filter: { updatedAt: {gt: $replicationKeyValue } }
        includeArchived: true
    ) {
        pageInfo {
            hasNextPage
            endCursor
        }
        nodes {
            id
            createdAt
            updatedAt
            editedAt
            archivedAt
            body
            url
            issue {
                id
                identifier
            }
            parent {
                id
            }
            user {
                id
                name
                email
            }
            externalUser {
                id
                name
            }
            botActor {
                name
                type
            }
        }
    }
}
"""
