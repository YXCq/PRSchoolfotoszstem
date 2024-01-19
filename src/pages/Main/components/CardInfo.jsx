import Photo from './Photo.png';
import {
    Button,
    Center,
    ChakraProvider,
    HStack,
    Image,
    SimpleGrid,
    VStack,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";

export const CardInfo = () => {
    const [allPhotos, setAllPhotos] = useState([]);
    const [selectedFiles, setSelectedFiles] = useState(null)

    return (
        <ChakraProvider>
            <Center>
                <VStack>
                    <HStack>
                        <input type="file" onChange={null} onClick={null} />
                        <Button size="lg" isDisable={null} onClick={null}>
                            Send our photos
                        </Button>
                    </HStack>
                    <SimpleGrid columns={3} spacing={8}>
                        {allPhotos.length !== 0 ? (
                            allPhotos.map((photo) => (
                                <Image
                                    key={photo.id}  // Add a unique key to each Image element
                                    borderRadius={25}
                                    boxSize="300px"
                                    src={photo["photo_url"]}
                                    fallbackSrc="https://via.placeholder.com/150"
                                    objectFit="cover"
                                />
                            ))
                        ) : (
                            <p>No photos available</p>
                        )}
                    </SimpleGrid>
                </VStack>
            </Center>
        </ChakraProvider>
    );
};
