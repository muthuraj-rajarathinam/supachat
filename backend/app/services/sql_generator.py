def generate_sql(query: str):
    query = query.lower()

    if "top" in query and "topic" in query:
        return """
        SELECT topic, SUM(views) as total_views
        FROM blog_analytics
        GROUP BY topic
        ORDER BY total_views DESC
        LIMIT 5;
        """

    if "ai" in query:
        return "SELECT * FROM blog_analytics WHERE topic='AI';"

    return "SELECT * FROM blog_analytics LIMIT 10;"