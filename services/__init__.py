"""
Services package for the Image Search App.
"""
from services.search_service import ImageSearchInterface, DummyImageSearch

__all__ = ['ImageSearchInterface', 'DummyImageSearch']