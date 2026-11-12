issuesQuery = """
query Issues($next: String, $replicationKeyValue: DateTimeOrDuration) {
    issues(
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
            identifier
            number
            title
            description
            url
            branchName
            priority
            priorityLabel
            estimate
            dueDate
            trashed
            customerTicketCount
            createdAt
            updatedAt
            startedAt
            completedAt
            canceledAt
            archivedAt
            triagedAt
            snoozedUntilAt
            slaStartedAt
            slaBreachesAt
            slaMediumRiskAt
            slaHighRiskAt
            slaType
            state {
                id
                name
                type
                color
                position
            }
            creator {
                id
                name
                email
            }
            assignee {
                id
                name
                email
            }
            parent {
                id
                identifier
                title
            }
            project {
                id
                name
            }
            projectMilestone {
                id
                name
                targetDate
            }
            team {
                id
                key
                name
            }
            cycle {
                id
                number
                name
                startsAt
                endsAt
            }
            labels {
                nodes {
                    id
                    name
                    color
                }
            }
            attachments {
                nodes {
                    id
                    url
                    title
                    subtitle
                    sourceType
                    source
                    metadata
                    createdAt
                }
            }
        }
    }
}
"""
