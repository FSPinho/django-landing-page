import React, { Component } from 'react'
import { connect } from 'react-redux'
import MobileDetect from 'mobile-detect'

import { Drawer, MenuItem } from 'material-ui'

class Sidenav extends Component {

    state = {
        opened: false
    }

    toggleDrawer = () => (this.setState({ opened: !this.state.opened }))
    close = () => (this.setState({ opened: false }))

    render() {
        const pageLinks = this.props.store.model.getIn(['model', 'page-link']).toJS()

        const mobileDetect = new MobileDetect(window.navigator.userAgent)
        const isMobile = !!mobileDetect.mobile()

        return (
            <Drawer
                docked={false}
                width={200}
                open={this.state.opened && isMobile}
                onRequestChange={(opened) => this.setState({ opened })}
            >
                {
                    pageLinks.map(pl => (
                        <MenuItem key={pl.page.name} onTouchTap={this.onMenuItemClicked}>{pl.page.name}</MenuItem>
                    ))
                }

            </Drawer>
        )
    }

}

export default connect((store) => ({ store }))(Sidenav)