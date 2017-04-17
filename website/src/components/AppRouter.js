import React, { Component } from 'react'
import { connect } from 'react-redux'
import { Route, Redirect } from 'react-router'
import { ConnectedRouter } from 'react-router-redux'
import getMuiTheme from 'material-ui/styles/getMuiTheme'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'

import { Page } from 'components'

class AppRouter extends Component {

    render() {

        const muiTheme = getMuiTheme({
            palette: {
            },
        })

        const pages = this.props.store.model.getIn(['model', 'page']).toJS()
        const defaultPage = pages.filter(p => p.mainPage)[0]

        return (
            <ConnectedRouter history={this.props.history}>
                <MuiThemeProvider muiTheme={muiTheme}>
                    <div>
                        {
                            pages.map(p => (

                                <Route exact key={p.id} path={`/${p.path}`.replace(/\/+/, '/')}
                                    render={props => (<Page {...props} page={p} />)}
                                >
                                </Route>
                            ))
                        }
                        {
                            defaultPage ? (
                                <Redirect exact form='/' to={`/${defaultPage.path}`.replace(/\/+/, '/')} />
                            ) : ('')
                        }
                    </div>
                </MuiThemeProvider>
            </ConnectedRouter>
        )
    }

}

export default connect((store) => ({ store }))(AppRouter)