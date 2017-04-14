import React, { Component } from 'react'

import { createStore, combineReducers, applyMiddleware } from 'redux'
import { Provider } from 'react-redux'

import createHistory from 'history/createBrowserHistory'

import { routerReducer, routerMiddleware } from 'react-router-redux'

import reducers from 'api/reducers'
import { AppRouter } from 'components';

class App extends Component {

	constructor(props) {
		super(props)

		this.history = createHistory()
		const middleware = routerMiddleware(history)
		this.store = createStore(
			combineReducers({
				...reducers,
				router: routerReducer
			}),
			applyMiddleware(middleware)
		)
	}

	render() {
		return (
			<Provider store={this.store}>

				<AppRouter history={this.history} />

			</Provider>
		)
	}
}

export default App
