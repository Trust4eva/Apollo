import * as React from 'react';
import { Socket } from './Socket';
import * as ReactDOM from 'react-dom';

export class Searchbar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'query' : '',
        };
        this.onFormSubmit = this.onFormSubmit.bind(this);
    }
    
     onTyping(event) {
        event.preventDefault();
        const text = event.target.value;
        if (text.length > 0) {
            this.setState(() => ({
                'query':text
            }));
        }
    }
    
    onFormSubmit(event) {
        event.preventDefault();
        console.log("query sent to server");
        Socket.emit('query created', {
            'query': this.state.query,
        });
    }
    
    render() {
        return (
        <form onSubmit={(e) => this.onFormSubmit(e)}>
        <input onChange={(e) => this.onTyping(e)} type= "text"/>
        <button>ENTER</button>
        </form> 
        );
    }
}