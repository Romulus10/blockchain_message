package io.github.romulus10.blckchnmsg;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.Collections;
import org.web3j.abi.TypeReference;
import org.web3j.abi.datatypes.Function;
import org.web3j.abi.datatypes.Type;
import org.web3j.abi.datatypes.Utf8String;
import org.web3j.crypto.Credentials;
import org.web3j.protocol.Web3j;
import org.web3j.protocol.core.RemoteCall;
import org.web3j.protocol.core.methods.response.TransactionReceipt;
import org.web3j.tx.Contract;
import org.web3j.tx.TransactionManager;

/**
 * <p>Auto generated code.
 * <p><strong>Do not modify!</strong>
 * <p>Please use the <a href="https://docs.web3j.io/command_line.html">web3j command line tools</a>,
 * or the org.web3j.codegen.SolidityFunctionWrapperGenerator in the 
 * <a href="https://github.com/web3j/web3j/tree/master/codegen">codegen module</a> to update.
 *
 * <p>Generated with web3j version 3.5.0.
 */
public class BlckChnMsgStorage extends Contract {
    private static final String BINARY = "608060405234801561001057600080fd5b50610547806100206000396000f30060806040526004361061004b5763ffffffff7c010000000000000000000000000000000000000000000000000000000060003504166370ef6e0b81146100505780637c252208146100b2575b600080fd5b34801561005c57600080fd5b50604080516020600460443581810135601f81018490048402850184019095528484526100b09482359460248035953695946064949201919081908401838280828437509497506101429650505050505050565b005b3480156100be57600080fd5b506100cd600435602435610190565b6040805160208082528351818301528351919283929083019185019080838360005b838110156101075781810151838201526020016100ef565b50505050905090810190601f1680156101345780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b80600083600a811061015057fe5b600a020184600a8110151561016157fe5b019080519060200190610175929190610480565b50606482600a811061018357fe5b0180546001019055505050565b606080600080606486600a81106101a357fe5b015491508490505b818110156102a45761029a83600088600a81106101c457fe5b600a020183600a811015156101d557fe5b01805460408051602060026001851615610100026000190190941693909304601f8101849004840282018401909252818152929183018282801561025a5780601f1061022f5761010080835404028352916020019161025a565b820191906000526020600020905b81548152906001019060200180831161023d57829003601f168201915b50505050506040805190810160405280600381526020017fe299a000000000000000000000000000000000000000000000000000000000008152506102ae565b92506001016101ab565b5090949350505050565b6060806060806060806000808a965089955088945084518651885101016040519080825280601f01601f1916602001820160405280156102f8578160200160208202803883390190505b50935083925060009150600090505b865181101561037d57868181518110151561031e57fe5b90602001015160f860020a900460f860020a02838380600101945081518110151561034557fe5b9060200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916908160001a905350600101610307565b5060005b85518110156103f757858181518110151561039857fe5b90602001015160f860020a900460f860020a0283838060010194508151811015156103bf57fe5b9060200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916908160001a905350600101610381565b5060005b845181101561047157848181518110151561041257fe5b90602001015160f860020a900460f860020a02838380600101945081518110151561043957fe5b9060200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916908160001a9053506001016103fb565b50909998505050505050505050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106104c157805160ff19168380011785556104ee565b828001600101855582156104ee579182015b828111156104ee5782518255916020019190600101906104d3565b506104fa9291506104fe565b5090565b61051891905b808211156104fa5760008155600101610504565b905600a165627a7a723058200ba97f5e124c171a8d94920f32c2290cfd80a8972371a52ef5f342f90fc6d0560029";

    public static final String FUNC_STORE = "store";

    public static final String FUNC_RETRIEVE = "retrieve";

    protected BlckChnMsgStorage(String contractAddress, Web3j web3j, Credentials credentials, BigInteger gasPrice, BigInteger gasLimit) {
        super(BINARY, contractAddress, web3j, credentials, gasPrice, gasLimit);
    }

    protected BlckChnMsgStorage(String contractAddress, Web3j web3j, TransactionManager transactionManager, BigInteger gasPrice, BigInteger gasLimit) {
        super(BINARY, contractAddress, web3j, transactionManager, gasPrice, gasLimit);
    }

    public RemoteCall<TransactionReceipt> store(BigInteger key, BigInteger to_user, String val) {
        final Function function = new Function(
                FUNC_STORE, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.generated.Uint256(key), 
                new org.web3j.abi.datatypes.generated.Uint256(to_user), 
                new org.web3j.abi.datatypes.Utf8String(val)), 
                Collections.<TypeReference<?>>emptyList());
        return executeRemoteCallTransaction(function);
    }

    public RemoteCall<String> retrieve(BigInteger to_user, BigInteger key) {
        final Function function = new Function(FUNC_RETRIEVE, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.generated.Uint256(to_user), 
                new org.web3j.abi.datatypes.generated.Uint256(key)), 
                Arrays.<TypeReference<?>>asList(new TypeReference<Utf8String>() {}));
        return executeRemoteCallSingleValueReturn(function, String.class);
    }

    public static RemoteCall<BlckChnMsgStorage> deploy(Web3j web3j, Credentials credentials, BigInteger gasPrice, BigInteger gasLimit) {
        return deployRemoteCall(BlckChnMsgStorage.class, web3j, credentials, gasPrice, gasLimit, BINARY, "");
    }

    public static RemoteCall<BlckChnMsgStorage> deploy(Web3j web3j, TransactionManager transactionManager, BigInteger gasPrice, BigInteger gasLimit) {
        return deployRemoteCall(BlckChnMsgStorage.class, web3j, transactionManager, gasPrice, gasLimit, BINARY, "");
    }

    public static BlckChnMsgStorage load(String contractAddress, Web3j web3j, Credentials credentials, BigInteger gasPrice, BigInteger gasLimit) {
        return new BlckChnMsgStorage(contractAddress, web3j, credentials, gasPrice, gasLimit);
    }

    public static BlckChnMsgStorage load(String contractAddress, Web3j web3j, TransactionManager transactionManager, BigInteger gasPrice, BigInteger gasLimit) {
        return new BlckChnMsgStorage(contractAddress, web3j, transactionManager, gasPrice, gasLimit);
    }
}
