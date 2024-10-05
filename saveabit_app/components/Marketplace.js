import {View, Button, Text} from 'react-native';

import { SearchBar } from 'react-native-elements';
import {useState} from "react";

export default function Marketplace(){

    const [search, useSearch] = useState('')
    useSearch=(search)=>{
        search=({search});
    };

    return(
        <View>  
            <Text>Your Listings</Text>

            <Button>Create New Listing</Button>

            {/* <SearchBar 
                placeholder="Type Here..."
                onChangeText={this.state.updateSearch}
                value={search}
            /> */}


            <>
            </>
        </View>
    )
}

