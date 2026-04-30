import streamlit as st

from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import generate_system_design
from pipeline.schema_generator import generate_final_schema
from pipeline.validator import validate_cross_layer
from pipeline.repair_engine import auto_repair


st.set_page_config(
    page_title="AI Compiler",
    layout="wide"
)

st.title("AI Compiler for Software Generation")

user_prompt = st.text_area(
    "Describe the application you want to build:",
    height=200
)

if st.button("Generate"):

    if user_prompt.strip():

        # Stage 1
        intent_result = extract_intent(user_prompt)

        if not intent_result["success"]:
            st.error(intent_result["error"])
            st.write(intent_result.get("raw_output"))
            st.stop()

        st.success("Stage 1 Complete: Intent Extraction")
        st.json(intent_result["data"])

        # Stage 2
        design_result = generate_system_design(
            intent_result["data"]
        )

        if not design_result["success"]:
            st.error(design_result["error"])
            st.write(design_result.get("raw_output"))
            st.stop()

        st.success("Stage 2 Complete: System Design")
        st.json(design_result["data"])

        # Stage 3
        final_result = generate_final_schema(
            intent_result["data"],
            design_result["data"]
        )

        if not final_result["success"]:
            st.error(final_result["error"])
            st.write(final_result.get("raw_output"))
            st.stop()

        st.success("Stage 3 Complete: Final Schema Generation")
        st.json(final_result["data"])

        # Stage 4
        validation_result = validate_cross_layer(
            final_result["data"]
        )

        if validation_result["success"]:
            st.success("Stage 4 Complete: Validation Passed")

        else:
            st.error("Validation Issues Found")
            st.write(validation_result["issues"])

            # Stage 5
            repaired_schema = auto_repair(
                final_result["data"],
                validation_result["issues"]
            )

            st.success("Stage 5 Complete: Auto Repair Applied")
            st.json(repaired_schema)

    else:
        st.warning("Please enter a prompt.")