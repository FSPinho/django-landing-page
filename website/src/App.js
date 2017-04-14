import React, { Component } from 'react'

import createHistory from 'history/createBrowserHistory'
import { createStore, combineReducers, applyMiddleware } from 'redux'
import { Provider } from 'react-redux'
import { routerReducer, routerMiddleware } from 'react-router-redux'
import createSagaMiddleware from 'redux-saga'

import reducers from 'api/reducers'
import sagas from 'api/sagas'
import { actions } from 'api/actions'
import { AppRouter } from 'components'

class App extends Component {

	constructor(props) {
		super(props)

		this.history = createHistory()
		const sagaMiddleware = createSagaMiddleware()

		this.store = createStore(
			combineReducers({
				...reducers,
				router: routerReducer,
			}),
			applyMiddleware(
				routerMiddleware(history),
				sagaMiddleware
			)
		)
		sagaMiddleware.run(sagas);

		this.store.dispatch({
			type: actions.model.do.load
		})
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
