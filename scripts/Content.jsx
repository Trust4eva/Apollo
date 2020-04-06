import * as React from 'react';
import { Searchbar } from './Searchbar';

export class Content extends React.Component {
    render() {
        return (
            <div>
            <h1>Apollo</h1>
            <Searchbar/>
            </div>
            );
    }
}