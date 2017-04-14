import React, { Component } from 'react'
import { connect } from 'react-redux'
import { Route } from 'react-router'
import { ConnectedRouter } from 'react-router-redux'
import getMuiTheme from 'material-ui/styles/getMuiTheme'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'

import { Page, Sidenav } from 'components'

class AppRouter extends Component {

    render() {

        const muiTheme = getMuiTheme({
            palette: {
            },
        })

        const pageLinks = this.props.store.model.getIn(['model', 'page-link']).toJS()

        return (
            <ConnectedRouter history={this.props.history}>
                <MuiThemeProvider muiTheme={muiTheme}>
                    <div>
                        <Sidenav />
                        {
                            pageLinks.map(pl => (
                                <Route exact key={pl.page.name} path={`/${pl.page.path}`.replace(/\/+/, '/')}
                                    render={props => (<Page {...props} page={pl.page} />)}
                                >
                                </Route>
                            ))
                        }
                    </div>
                </MuiThemeProvider>
            </ConnectedRouter>
        )
    }

}

export default connect((store) => ({ store }))(AppRouter)