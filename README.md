## Architecture

The application follows a modular architecture with dependency injection and composition at its core. The architecture is designed to ensure:

- **Separation of concerns**: Each component has a single responsibility
- **Testability**: Components can be tested in isolation
- **Extensibility**: Easy to add or replace features
- **Maintainability**: Clean code structure with clear dependencies

### Architectural Diagram

```
┌───────────────────────────────────────────────────────────┐
│                          main.py                          │
│                                                           │
│  Creates dependencies and injects them into components    │
└─────────────────┬────────────────────────┬────────────────┘
                  │                        │
┌─────────────────▼─────┐       ┌──────────▼────────────┐
│      config.py        │       │       app_state.py    │
│                       │       │                       │
│  Application settings │       │  Session state mgmt   │
└─────────────────┬─────┘       └──────────┬────────────┘
                  │                        │
                  │                        │
┌─────────────────▼────────────────────────▼────────────────┐
│                      Services                             │
│                                                           │
│  ┌────────────────────┐     ┌───────────────────────┐     │
│  │  search_service.py │     │    image_data.py      │     │
│  │                    │     │                       │     │
│  │  Image searching   │     │  Image data storage   │     │
│  └────────┬───────────┘     └───────────┬───────────┘     │
└───────────┼─────────────────────────────┼─────────────────┘
            │                             │                  
┌───────────▼─────────────────────────────▼─────────────────┐
│                           UI                              │
│                                                           │
│  ┌────────────────┐   ┌────────────────┐   ┌───────────┐  │
│  │  navigation.py │   │  components/   │   │  pages/   │  │
│  │                │   │                │   │           │  │
│  │  Sidebar and   │   │  UI building   │   │  Page     │  │
│  │  navigation    │   │  blocks        │   │  layouts  │  │
│  └────────────────┘   └────────────────┘   └───────────┘  │
└───────────────────────────────────────────────────────────┘
```

### Component Interactions

1. **Main Entry Point**: `main.py` initializes the application, creates services, sets up the UI, and starts the navigation system.

2. **Configuration**: `config.py` provides centralized configuration for the application.

3. **Services**: Responsible for business logic like image searching and data storage.

4. **UI Components**: Reusable UI building blocks that can be composed to create pages.

5. **Pages**: Complete views composed of multiple UI components.

6. **Navigation**: Manages the sidebar and switching between pages.

7. **App State**: Handles Streamlit session state for persisting data between interactions.

## Components Description

### Configuration (`config.py`)

**Purpose**: Centralize application configuration settings.

**Key Functions**:
- `AppConfig`: Class that contains all configuration parameters.

**Dependencies**: None

### Models

#### Image Data Store (`models/image_data.py`)

**Purpose**: Manage storage and retrieval of image selection data.

**Key Functions**:
- `save_clicked_image()`: Save information about clicked images
- `_load_data()`: Load image data from JSON
- `_save_data()`: Save image data to JSON

**Dependencies**: 
- File system (JSON)

### Services

#### Search Service (`services/search_service.py`)

**Purpose**: Provide search functionality for images.

**Key Functions**:
- `ImageSearchInterface`: Abstract interface for image search
- `DummyImageSearch`: Concrete implementation that returns random images
- `search()`: Search method that returns matching images

**Dependencies**:
- File system (images folder)

### UI Components

#### Search Bar (`ui/components/search_bar.py`)

**Purpose**: Render search input field and options.

**Key Functions**:
- `render()`: Display the search bar and handle user input

**Dependencies**:
- Streamlit
- Search callback function

#### Image Grid (`ui/components/image_grid.py`)

**Purpose**: Display search results in a grid layout.

**Key Functions**:
- `render()`: Display images in a grid with selection buttons

**Dependencies**:
- Streamlit
- PIL (Pillow)
- Image click callback function

#### Help Section (`ui/components/help_section.py`)

**Purpose**: Display help information for users.

**Key Functions**:
- `render()`: Display expandable help information

**Dependencies**:
- Streamlit

### Pages

#### Image Search Page (`ui/pages/image_search_page.py`)

**Purpose**: Render the main image search functionality.

**Key Functions**:
- `render()`: Display the search page
- `handle_search()`: Handle search requests
- `handle_image_click()`: Handle image selection

**Dependencies**:
- Search Bar component
- Image Grid component
- Help Section component
- Search Service
- Image Data Store

#### Upload Page (`ui/pages/upload_page.py`)

**Purpose**: Allow users to upload new images.

**Key Functions**:
- `render()`: Display the upload page
- `_save_uploaded_image()`: Save uploaded images

**Dependencies**:
- Streamlit
- PIL (Pillow)
- File system

#### Analytics Page (`ui/pages/analytics_page.py`)

**Purpose**: Display analytics about search patterns.

**Key Functions**:
- `render()`: Display the analytics page
- `_get_analytics_data()`: Process and extract analytics data

**Dependencies**:
- Streamlit
- Pandas
- Matplotlib
- Image Data Store

### Navigation (`ui/navigation.py`)

**Purpose**: Manage the sidebar navigation and page switching.

**Key Functions**:
- `render()`: Display the navigation sidebar
- `add_tab()`: Add a new tab to the navigation
- `add_button()`: Add a new action button

**Dependencies**:
- Streamlit

### App State (`app_state.py`)

**Purpose**: Manage Streamlit session state for the application.

**Key Functions**:
- `initialize_session_state()`: Set up default session state
- `clear_search_history()`: Clear search history

**Dependencies**:
- Streamlit

## Getting Started

### Prerequisites

- Python 3.7+
- Streamlit
- Pillow (PIL)
- Pandas
- Matplotlib

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Faisal-Hajari/text2image.git
cd text2image
```

2. Create and activate a virtual environment (optional but recommended):

```bash
# Using conda
conda create -n text2image python=3.12
conda activate text2image
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

### Running the Application

Run the app with Streamlit:

```bash
streamlit run main.py
```

The application will start and be available at http://localhost:8501.

### Project Structure

```
image-search-app/
├── main.py                  # Application entry point
├── config.py                # Configuration settings
├── app_state.py             # Session state management
├── requirements.txt         # Dependencies
├── models/                  # Data models
│   ├── __init__.py
│   └── image_data.py        # Image data storage
├── services/                # Business logic
│   ├── __init__.py
│   └── search_service.py    # Search functionality
└── ui/                      # User interface
    ├── __init__.py
    ├── navigation.py        # Navigation system
    ├── components/          # Reusable UI components
    │   ├── __init__.py
    │   ├── search_bar.py    # Search input component
    │   ├── image_grid.py    # Image display component
    │   └── help_section.py  # Help information component
    └── pages/               # Application pages
        ├── __init__.py
        ├── image_search_page.py  # Main search page
        ├── upload_page.py        # Image upload page
        └── analytics_page.py     # Analytics page
```

## How to Contribute

### Adding New Features

The modular architecture makes it easy to add new features:

1. **Add a new page**:
   - Create a new file in the `ui/pages/` directory
   - Implement a class with a `render()` method
   - Add the page to the navigation in `main.py`

2. **Add a new component**:
   - Create a new file in the `ui/components/` directory
   - Implement a class with a `render()` method
   - Use the component in a page

3. **Add a new service**:
   - Create a new file in the `services/` directory
   - Implement the necessary business logic
   - Inject the service into the appropriate components

### Implementing a Real Search Service

The current implementation uses a dummy search service that returns random images. To implement a real search service:

1. Create a new class that implements `ImageSearchInterface` in `services/search_service.py`
2. Implement the `search()` method with real search logic
3. Update `main.py` to use your new search service

Example:

```python
class RealImageSearch(ImageSearchInterface):
    def __init__(self, image_folder: str) -> None:
        self.image_folder = image_folder
        # Initialize any search indexing here
        
    def search(self, query: str, num_results: int = 5) -> List[str]:
        # Implement real search logic here
        # Return a list of image paths that match the query
        return matching_images
```

### Adding a New Page

To add a new page to the application:

1. Create a new file in the `ui/pages/` directory:

```python
# ui/pages/new_feature_page.py
import streamlit as st

class NewFeaturePage:
    def __init__(self, dependency1, dependency2) -> None:
        self.dependency1 = dependency1
        self.dependency2 = dependency2
    
    def render(self) -> None:
        st.title("New Feature")
        # Implement your page UI here
```

2. Update `ui/pages/__init__.py` to import your new page:

```python
from ui.pages.new_feature_page import NewFeaturePage

__all__ = [..., 'NewFeaturePage']
```

3. Add the page to the navigation in `main.py`:

```python
# Create page instance
new_feature_page = NewFeaturePage(dependency1, dependency2)

# Add to navigation
navigation = Navigation(
    title="Navigation",
    tabs={
        # Existing tabs...
        "New Feature": new_feature_page.render,
    },
    buttons={
        "Clear History": clear_search_history
    }
)
```

### Code Style Guidelines

- Follow PEP 8 for Python code style
- Use type hints (Python 3.7+)
- Write comprehensive docstrings using Google style
- Keep methods small and focused on a single responsibility

## Examples

### Using the Image Search

1. Start the application with `streamlit run main.py`
2. Navigate to the "Search Images" tab
3. Enter a search query and select the number of results
4. Click "Search" to see matching images
5. Click "Select" under an image to save it to your selections

### Uploading Images

1. Navigate to the "Upload Images" tab
2. Click "Browse files" to select images from your computer
3. Upload one or more images
4. The uploaded images will appear in the gallery and be available for search

### Viewing Analytics

1. Use the application to search for and select images
2. Navigate to the "Analytics" tab
3. View statistics about top search queries and selected images

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Streamlit for providing the web application framework
- The Python community for the excellent libraries used in this project