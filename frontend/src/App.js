import './App.css';
import Header from './components/Header';
import NotesListPage from './pages/NotesListPage';
import NotePage from './pages/NotePage';
import { 
	HashRouter as Router,		// here we have used HashRouter instead of BrowserRouter to fix the issue "url not found" when we refresh a page
	Route, 
	Routes
} from "react-router-dom";

function App() {
	return (
		<Router>
		<div className="container dark">
			<div className='app'>
				<Header/>
				<Routes>
					<Route exact path="/" element={<NotesListPage />} />
					<Route path="/note/:id" element={<NotePage />} />
				</Routes>
			</div>
		</div>
		</Router>
	);
}

export default App;
