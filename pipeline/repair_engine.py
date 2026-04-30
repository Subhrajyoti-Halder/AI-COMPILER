def auto_repair(final_schema: dict, issues: list):
    """
    Automatically repair simple validation issues
    without full regeneration.
    """

    repaired = final_schema.copy()

    db_tables = repaired.get("db_tables", [])
    db_table_names = [table["name"] for table in db_tables]

    for issue in issues:

        # Fix missing DB table for API path
        if "does not map to DB table" in issue:
            path = issue.split("'")[1]
            table_name = path.replace("/", "").strip()

            if table_name and table_name not in db_table_names:
                repaired["db_tables"].append({
                    "name": table_name,
                    "fields": [
                        "id",
                        "name",
                        "created_at"
                    ]
                })

    return repaired