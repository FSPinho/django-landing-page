import React, { Component } from 'react'
import { connect } from 'react-redux'
import MobileDetect from 'mobile-detect'
import { AppBar, Drawer, MenuItem, Toolbar, ToolbarGroup, ToolbarTitle, FlatButton, RaisedButton } from 'material-ui'
import muiThemeable from 'material-ui/styles/muiThemeable'
import { fade } from 'material-ui/utils/colorManipulator';

import { Section, Footer } from 'components'

class Page extends Component {

    state = {
        drawer: {
            opened: false
        },
        toolbar: {
            scrollTop: 0
        }
    }

    setDrawerState = state => (this.setState({ drawer: { opened: state } }))
    toggleDrawer = () => (this.setDrawerState(!this.state.drawer.opened))
    close = () => (this.setState(false))

    onPageLinkClicked = page => {
        console.log(page)
    }

    componentDidMount() {
        window.onscroll = () => {
            this.setState({ toolbar: { scrollTop: window.pageYOffset } })
        }
    }

    render() {
        const theme = this.props.muiTheme
        const pages = this.props.store.model.getIn(['model', 'page']).toJS()
            .sort((a, b) => (
                a.mainPage ? -1 : (b.mainPage ? 1 : (a.order - b.order))
            ))
        const page = this.props.page
        const footer = page.footer

        const sections = page.sections.sort((a, b) => (
            a.order - b.order
        ))

        const _getOpacityFrom = scroll => (
            (Math.exp(0.01 * scroll) - Math.exp(0.01 * -scroll)) /
            (Math.exp(0.01 * scroll) + Math.exp(0.01 * -scroll))
        )
        const currentScroll = this.state.toolbar.scrollTop
        const toolbarOpacity = currentScroll >= 100 ? 1.0 : _getOpacityFrom(currentScroll)


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
                        pages.map(p => (
                            <MenuItem key={p.name} onTouchTap={() => this.onPageLinkClicked(p)}>{p.name}</MenuItem>
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
                                    position: 'fixed',
                                    zIndex: 1000,
                                    left: 0,
                                    right: 0,
                                    backgroundColor: fade(this.props.muiTheme.palette.primary1Color, toolbarOpacity),
                                }}>
                                <ToolbarGroup firstChild={true}>
                                    <ToolbarTitle style={{
                                        marginLeft: 20,
                                        color: this.props.muiTheme.palette.alternateTextColor
                                    }} text={page.name} />
                                </ToolbarGroup>
                                <ToolbarGroup>
                                    {
                                        pages.filter(p => p.showInNavigation).map(p => (

                                            <FlatButton key={p.name}
                                                style={{
                                                    color: this.props.muiTheme.palette.alternateTextColor,
                                                    marginLeft: 10,
                                                    marginRight: 0,
                                                }}
                                                label={p.name}
                                                onTouchTap={() => this.onPageLinkClicked(p)} />)
                                        )
                                    }
                                </ToolbarGroup>
                            </Toolbar>
                        )
                }
                {
                    page.sections.map(section => (
                        <Section key={section.id} section={section} />
                    ))
                }
                {
                    footer ? (<Footer footer={footer} />) : ('')
                }
            </div>
        )
    }

}

const PageThemeable = muiThemeable()(Page)
export default connect((store) => ({ store }))(PageThemeable)