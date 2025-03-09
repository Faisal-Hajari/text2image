"""
Main entry point for the Image Search App.

This module creates and configures all necessary components and starts the application.
"""
import streamlit as st
from functools import partial

from config import AppConfig
from services.search_service import DummyImageSearch
from models.image_data import ImageDataStore
from ui.navigation import Navigation, custom_sidebar_style
from ui.pages.image_search_page import ImageSearchPage
from ui.pages.analytics_page import AnalyticsPage
from ui.pages.upload_page import UploadPage
from app_state import initialize_session_state, clear_search_history


def main() -> None:
    """
    Main entry point for the application.
    
    Creates all necessary components using dependency injection and runs the app.
    """
    # Set up page configuration
    st.set_page_config(
        page_title="Image Search App",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Apply custom sidebar style
    custom_sidebar_style()
    
    # Initialize session state
    initialize_session_state()
    
    # Create configuration
    config = AppConfig()
    
    # Create services
    search_service = DummyImageSearch(config.image_folder)
    data_store = ImageDataStore(config.json_file)
    
    # Create page instances
    search_page = ImageSearchPage(config, search_service, data_store)
    analytics_page = AnalyticsPage(data_store)
    upload_page = UploadPage(config)
    
    # Create navigation with tabs
    navigation = Navigation(
        title="Navigation",
        tabs={
            "Search Images": search_page.render,
            "Upload Images": upload_page.render,
            "Analytics": analytics_page.render,
        },
        buttons={
            "Clear History": clear_search_history
        }
    )
    
    # Render the navigation and selected page
    navigation.render()


if __name__ == "__main__":
    main()