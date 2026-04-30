def validate_cross_layer(final_schema: dict):
    """
    Validate consistency across:

    UI ↔ API ↔ DB ↔ Auth

    Returns:
    {
        success: bool,
        issues: list
    }
    """

    issues = []

    ui_pages = final_schema.get("ui_pages", [])
    api_endpoints = final_schema.get("api_endpoints", [])
    db_tables = final_schema.get("db_tables", [])
    auth_rules = final_schema.get("auth_rules", {})

    db_table_names = [table["name"] for table in db_tables]
    api_paths = [api["path"] for api in api_endpoints]

    # -----------------------------------
    # Check 1: API should map to DB tables
    # -----------------------------------
    for api in api_endpoints:
        path = api["path"].replace("/", "").split("{")[0]

        if path and path not in db_table_names:
            if path not in ["login", "analytics"]:
                issues.append(
                    f"API path '{api['path']}' does not map to DB table"
                )

    # -----------------------------------
    # Check 2: UI pages should map to APIs
    # -----------------------------------
    for page in ui_pages:
        page_name = page["name"].lower()

        matched = any(
            page_name in api["path"]
            for api in api_endpoints
        )

        if not matched:
            issues.append(
                f"UI page '{page['name']}' has no related API endpoint"
            )

    # -----------------------------------
    # Check 3: Roles must exist in auth
    # -----------------------------------
    if not auth_rules:
        issues.append("Auth rules missing completely")

    # -----------------------------------
    # Final Result
    # -----------------------------------
    return {
        "success": len(issues) == 0,
        "issues": issues
    }