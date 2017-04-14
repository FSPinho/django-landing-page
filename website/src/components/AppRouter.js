import React, { Component } from 'react'
import { connect } from 'react-redux'

import { Route } from 'react-router'

import { ConnectedRouter } from 'react-router-redux'

class AppRouter extends Component {

    render() {
        return (
            <ConnectedRouter history={this.props.history}>
                <div>
                    <Route exact path="/" component={null} />
                    <Route path="/about" component={null} />
                    <Route path="/topics" component={null} />
                </div>
            </ConnectedRouter>
        )
    }

}

export default connect(({ store }) => ({ store }))(AppRouter)