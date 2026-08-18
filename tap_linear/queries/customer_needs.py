customerNeedsQuery = """
query CustomerNeeds($next: String, $replicationKeyValue: DateTimeOrDuration) {
    customerNeeds(
        first: 50
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
            archivedAt
            priority
            body
            url
            customer {
                id
                name
                externalIds
                domains
                revenue
                size
                tier {
                    id
                    name
                }
                status {
                    id
                    name
                }
            }
            issue {
                id
                identifier
            }
            originalIssue {
                id
                identifier
            }
            project {
                id
                name
            }
            creator {
                id
                name
                email
            }
        }
    }
}
"""
