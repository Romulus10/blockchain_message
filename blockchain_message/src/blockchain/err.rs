use std::error;
use std::fmt;

#[derive(Debug)]
pub struct InsertionFailure {
    pub v: String,
}

pub type InsertionFailureError = InsertionFailure;

impl fmt::Display for InsertionFailureError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.v)
    }
}

impl error::Error for InsertionFailureError {
    fn description(&self) -> &str {
        "The Keyword Could Not Be Identified"
    }
}

#[derive(Debug)]
pub struct DeletionFailure {
    pub v: String,
}

pub type DeletionFailureError = DeletionFailure;

impl fmt::Display for DeletionFailureError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.v)
    }
}

impl error::Error for DeletionFailureError {
    fn description(&self) -> &str {
        "The Keyword Could Not Be Identified"
    }
}

#[derive(Debug)]
pub struct UpdateFailure {
    pub v: String,
}

pub type UpdateFailureError = UpdateFailure;

impl fmt::Display for UpdateFailureError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.v)
    }
}

impl error::Error for UpdateFailureError {
    fn description(&self) -> &str {
        "The Keyword Could Not Be Identified"
    }
}

#[derive(Debug)]
pub struct ReadFailure {
    pub v: String,
}

pub type ReadFailureError = ReadFailure;

impl fmt::Display for ReadFailureError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.v)
    }
}

impl error::Error for ReadFailureError {
    fn description(&self) -> &str {
        "The Keyword Could Not Be Identified"
    }
}

#[derive(Debug)]
pub enum BlockchainError {
    CouldNotInsertData(InsertionFailureError),
    CouldNotDeleteData(DeletionFailureError),
    CouldNotUpdateData(UpdateFailureError),
    CouldNotReadData(ReadFailureError),
}

impl fmt::Display for BlockchainError {
    
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            BlockchainError::CouldNotInsertData(ref err) => {
                write!(f, "Could not open Insert Data {}", err)
            }
            BlockchainError::CouldNotDeleteData(ref err) => {
                write!(f, "Could Not Delete Data {}", err)
            }
            BlockchainError::CouldNotUpdateData(ref err) => {
                write!(f, "Could Not Update Data {}", err)
            }
            BlockchainError::CouldNotReadData(ref err) => {
                write!(f, "Could Not Read Data {}", err)
            }
        
        }
    }
}

impl error::Error for BlockchainError {
    fn description(&self) -> &str {
        match *self {
            BlockchainError::CouldNotInsertData(ref err) => err.description(),
            BlockchainError::CouldNotDeleteData(ref err) => err.description(),
            BlockchainError::CouldNotUpdateData(ref err) => err.description(),
            BlockchainError::CouldNotReadData(ref err) => err.description(),
        }
    }
   
    fn cause(&self) -> Option<&error::Error> {
        match *self {
            BlockchainError::CouldNotInsertData(ref err) => Some(err),
            BlockchainError::CouldNotDeleteData(ref err) => Some(err),
            BlockchainError::CouldNotUpdateData(ref err) => Some(err),
            BlockchainError::CouldNotReadData(ref err) => Some(err),
        }
    }
}

impl From<InsertionFailureError> for BlockchainError {
    fn from(err: InsertionFailureError) -> BlockchainError {
        BlockchainError::CouldNotInsertData(err)
    }
}

impl From<DeletionFailureError> for BlockchainError {
    fn from(err: DeletionFailureError) -> BlockchainError {
        BlockchainError::CouldNotDeleteData(err)
    }
}

impl From<UpdateFailureError> for BlockchainError {
    fn from(err: UpdateFailureError) -> BlockchainError {
        BlockchainError::CouldNotUpdateData(err)
    }
}

impl From<ReadFailureError> for BlockchainError {
    fn from(err: ReadFailureError) -> BlockchainError {
        BlockchainError::CouldNotReadData(err)
    }
}

