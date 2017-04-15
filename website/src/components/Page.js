import React, { Component } from 'react'
import { connect } from 'react-redux'
import MobileDetect from 'mobile-detect'
import { AppBar, Drawer, MenuItem, Toolbar, ToolbarGroup, ToolbarTitle, FlatButton, RaisedButton } from 'material-ui'
import muiThemeable from 'material-ui/styles/muiThemeable';

class Page extends Component {

    state = {
        drawer: {
            opened: false
        }
    }

    setDrawerState = state => (this.setState({ drawer: { opened: state } }))
    toggleDrawer = () => (this.setDrawerState(!this.state.drawer.opened))
    close = () => (this.setState(false))

    onPageLinkClicked = pageLink => {
        console.log(pageLink)
    }

    render() {
        const pages = this.props.store.model.getIn(['model', 'page']).toJS()
        const page = pages.filter(p => (p.name === this.props.page.name))[0]
        const pageLinks = this.props.store.model.getIn(['model', 'page-link']).toJS()
            .sort((a, b) => (
                a.page.mainPage? -1: (b.page.mainPage? 1: (a.order - b.order))
            )) 

        const mobileDetect = new MobileDetect(window.navigator.userAgent)
        const isMobile = !!mobileDetect.mobile()

        return (
            <div>
                <Drawer
                    docked={false}
                    width={200}
                    open={this.state.drawer.opened && isMobile}
                    onRequestChange={this.setDrawerState}
                >
                    {
                        pageLinks.map(pl => (
                            <MenuItem key={pl.page.name} onTouchTap={() => this.onPageLinkClicked(pl)}>{pl.page.name}</MenuItem>
                        ))
                    }

                </Drawer>
                {
                    isMobile ? (
                        <AppBar
                            title={page.name}
                            iconClassNameRight="muidocs-icon-navigation-expand-more"
                            onLeftIconButtonTouchTap={this.toggleDrawer}
                        />
                    ) : (
                            <Toolbar
                                style={{
                                    backgroundColor: this.props.muiTheme.palette.primary1Color
                                }}>
                                <ToolbarGroup firstChild={true}>
                                    <ToolbarTitle style={{
                                        marginLeft: 20,
                                        color: this.props.muiTheme.palette.alternateTextColor
                                    }} text={page.name} />
                                </ToolbarGroup>
                                <ToolbarGroup>
                                    {
                                        pageLinks.map(pl => (
                                            pl.appearance === 'text' ? (
                                                <FlatButton key={pl.page.name}
                                                    style={{
                                                        color: this.props.muiTheme.palette.alternateTextColor,
                                                        marginLeft: 10,
                                                        marginRight: 0,
                                                    }}
                                                    label={pl.page.name}
                                                    onTouchTap={() => this.onPageLinkClicked(pl)} />
                                            ) : (
                                                    <RaisedButton key={pl.page.name}
                                                        style={{
                                                            color: this.props.muiTheme.palette.alternateTextColor,
                                                            marginLeft: 10,
                                                            marginRight: 0,
                                                        }}
                                                        primary={pl.color === 'primary'}
                                                        secondary={pl.color === 'accent'}
                                                        label={pl.page.name}
                                                        onTouchTap={() => this.onPageLinkClicked(pl)} />
                                                )
                                        ))
                                    }
                                </ToolbarGroup>
                            </Toolbar>
                        )
                }
            </div>
        )
    }

}

const PageThemeable = muiThemeable()(Page)
export default connect((store) => ({ store }))(PageThemeable)