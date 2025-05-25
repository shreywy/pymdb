
# *[WIP] A lightweight Python app to track shows/kdrama (and later AniManga).*  

### Development Phases  

**Phase 1: Backend + CLI Prototype** *(Mostly Done)*  
- Read API key from `key.txt`  
- Search TMDb, display results (title + ID)  
- Save/Load shows to `storage.json`  
- **Add:**  
  - View show details (TMDb fetch)  
  - Add/edit ratings, watch status, notes  
  - Remove shows  
  - Filter/sort by status/rating  
  - Improved formatting *(optional, GUI replaces later)*  

**Phase 2: Basic PyWebView Setup**  
- Launch window with `index.html` placeholder  
- Test Python / JS communication  

**Phase 3: Search UI + Integration**  
- Frontend search bar → TMDb API calls  
- Display results with posters  
- Save selections to `storage.json`  

**Phase 4: Show Details + Editing UI**  
- Popup for:  
  - Title, poster, description  
  - Editable rating/status/notes  
- Save edits locally  

**Phase 5: Dashboard UI**  
- Grid of saved shows (thumbnails + titles)  
- Click to open details/edit view  
- Minimal, sleek design (CSS grid)  

---