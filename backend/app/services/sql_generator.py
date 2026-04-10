def generate_sql(query: str):
    query = query.lower()

    # 🔹 Top topics
    if "top" in query and "topic" in query:
        return """
        SELECT topic, SUM(views) as total_views
        FROM blog_analytics
        GROUP BY topic
        ORDER BY total_views DESC
        LIMIT 5;
        """

    # 🔹 Top blogs (by views / likes / comments)
    if "top" in query or "best" in query:
        if "likes" in query:
            return """
            SELECT * FROM blog_analytics
            ORDER BY likes DESC
            LIMIT 5;
            """
        elif "comments" in query:
            return """
            SELECT * FROM blog_analytics
            ORDER BY comments DESC
            LIMIT 5;
            """
        else:
            return """
            SELECT * FROM blog_analytics
            ORDER BY views DESC
            LIMIT 5;
            """

    # 🔹 Topic-based filtering
    topics = ["ai", "devops", "frontend", "backend", "cloud", "security", "database", "data", "mobile", "design", "startup"]
    for topic in topics:
        if topic in query:
            return f"""
            SELECT * FROM blog_analytics
            WHERE LOWER(topic) = '{topic}';
            """

    # 🔹 Trending (recent + high views)
    if "trending" in query or "recent" in query:
        return """
        SELECT *
        FROM blog_analytics
        WHERE created_at >= NOW() - INTERVAL '7 days'
        ORDER BY views DESC
        LIMIT 10;
        """

    # 🔹 Most discussed
    if "discussion" in query or "comment" in query:
        return """
        SELECT *
        FROM blog_analytics
        ORDER BY comments DESC
        LIMIT 10;
        """

    # 🔹 Engagement (likes + comments)
    if "engagement" in query:
        return """
        SELECT *, (likes + comments) AS engagement
        FROM blog_analytics
        ORDER BY engagement DESC
        LIMIT 10;
        """

    # 🔹 Search by title keyword
    if "search" in query or "find" in query:
        words = query.split()
        keyword = words[-1]  # simple assumption
        return f"""
        SELECT *
        FROM blog_analytics
        WHERE LOWER(title) LIKE '%{keyword}%';
        """

    # 🔹 Date filtering
    if "last 30 days" in query:
        return """
        SELECT *
        FROM blog_analytics
        WHERE created_at >= NOW() - INTERVAL '30 days';
        """

    if "today" in query:
        return """
        SELECT *
        FROM blog_analytics
        WHERE DATE(created_at) = CURRENT_DATE;
        """

    # 🔹 Default fallback
    return "SELECT * FROM blog_analytics LIMIT 10;"
