import gql from "../_gql";
import makeRequest from "../makeRequest";

const query = gql`
    mutation DeleteAccount($target: String) {
        deleteAccount(target: $target)
    }
`;

export default async (target: Optional<string>): Promise<string> => {
    return makeRequest(query, { target });
};
