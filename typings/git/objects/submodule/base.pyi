"""
This type stub file was generated by pyright.
"""

from git.config import SectionConstraint
from git.objects.base import IndexObject
from git.objects.util import TraversableIterableObj
from git.util import IterableList, RemoteProgress, unbare_repo
from .util import SubmoduleConfigParser
from typing import Any, Iterator, Mapping, Sequence, TYPE_CHECKING, Union
from git.types import Commit_ish, Literal, PathLike, TBD
from git.index import IndexFile
from git.repo import Repo
from git.refs import Head

if TYPE_CHECKING: ...
__all__ = ["Submodule", "UpdateProgress"]
log = ...

class UpdateProgress(RemoteProgress):
    """Class providing detailed progress information to the caller who should
    derive from it and implement the ``update(...)`` message"""

    _num_op_codes: int = ...
    __slots__ = ...

BEGIN = ...
END = ...
CLONE = ...
FETCH = ...
UPDWKTREE = ...

class Submodule(IndexObject, TraversableIterableObj):
    """Implements access to a git submodule. They are special in that their sha
    represents a commit in the submodule's repository which is to be checked out
    at the path of this instance.
    The submodule type does not have a string type associated with it, as it exists
    solely as a marker in the tree and index.

    All methods work in bare and non-bare repositories."""

    _id_attribute_ = ...
    k_modules_file = ...
    k_head_option = ...
    k_head_default = ...
    k_default_mode = ...
    type: Literal[submodule] = ...
    __slots__ = ...
    _cache_attrs = ...
    def __init__(
        self,
        repo: Repo,
        binsha: bytes,
        mode: Union[int, None] = ...,
        path: Union[PathLike, None] = ...,
        name: Union[str, None] = ...,
        parent_commit: Union[Commit_ish, None] = ...,
        url: Union[str, None] = ...,
        branch_path: Union[PathLike, None] = ...,
    ) -> None:
        """Initialize this instance with its attributes. We only document the ones
        that differ from ``IndexObject``

        :param repo: Our parent repository
        :param binsha: binary sha referring to a commit in the remote repository, see url parameter
        :param parent_commit: see set_parent_commit()
        :param url: The url to the remote repository which is the submodule
        :param branch_path: full (relative) path to ref to checkout when cloning the remote repository
        """
        ...
    def __eq__(self, other: Any) -> bool:
        """Compare with another submodule"""
        ...
    def __ne__(self, other: object) -> bool:
        """Compare with another submodule for inequality"""
        ...
    def __hash__(self) -> int:
        """Hash this instance using its logical id, not the sha"""
        ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    @classmethod
    def add(
        cls,
        repo: Repo,
        name: str,
        path: PathLike,
        url: Union[str, None] = ...,
        branch: Union[str, None] = ...,
        no_checkout: bool = ...,
        depth: Union[int, None] = ...,
        env: Union[Mapping[str, str], None] = ...,
        clone_multi_options: Union[Sequence[TBD], None] = ...,
        allow_unsafe_options: bool = ...,
        allow_unsafe_protocols: bool = ...,
    ) -> Submodule:
        """Add a new submodule to the given repository. This will alter the index
        as well as the .gitmodules file, but will not create a new commit.
        If the submodule already exists, no matter if the configuration differs
        from the one provided, the existing submodule will be returned.

        :param repo: Repository instance which should receive the submodule
        :param name: The name/identifier for the submodule
        :param path: repository-relative or absolute path at which the submodule
            should be located
            It will be created as required during the repository initialization.
        :param url: git-clone compatible URL, see git-clone reference for more information
            If None, the repository is assumed to exist, and the url of the first
            remote is taken instead. This is useful if you want to make an existing
            repository a submodule of anotherone.
        :param branch: name of branch at which the submodule should (later) be checked out.
            The given branch must exist in the remote repository, and will be checked
            out locally as a tracking branch.
            It will only be written into the configuration if it not None, which is
            when the checked out branch will be the one the remote HEAD pointed to.
            The result you get in these situation is somewhat fuzzy, and it is recommended
            to specify at least 'master' here.
            Examples are 'master' or 'feature/new'
        :param no_checkout: if True, and if the repository has to be cloned manually,
            no checkout will be performed
        :param depth: Create a shallow clone with a history truncated to the
            specified number of commits.
        :param env: Optional dictionary containing the desired environment variables.
            Note: Provided variables will be used to update the execution
            environment for `git`. If some variable is not specified in `env`
            and is defined in `os.environ`, value from `os.environ` will be used.
            If you want to unset some variable, consider providing empty string
            as its value.
        :param clone_multi_options: A list of Clone options. Please see ``git.repo.base.Repo.clone``
            for details.
        :param allow_unsafe_protocols: Allow unsafe protocols to be used, like ext
        :param allow_unsafe_options: Allow unsafe options to be used, like --upload-pack
        :return: The newly created submodule instance
        :note: works atomically, such that no change will be done if the repository
            update fails for instance"""
        ...
    def update(
        self,
        recursive: bool = ...,
        init: bool = ...,
        to_latest_revision: bool = ...,
        progress: Union[UpdateProgress, None] = ...,
        dry_run: bool = ...,
        force: bool = ...,
        keep_going: bool = ...,
        env: Union[Mapping[str, str], None] = ...,
        clone_multi_options: Union[Sequence[TBD], None] = ...,
        allow_unsafe_options: bool = ...,
        allow_unsafe_protocols: bool = ...,
    ) -> Submodule:
        """Update the repository of this submodule to point to the checkout
        we point at with the binsha of this instance.

        :param recursive: if True, we will operate recursively and update child-
            modules as well.
        :param init: if True, the module repository will be cloned into place if necessary
        :param to_latest_revision: if True, the submodule's sha will be ignored during checkout.
            Instead, the remote will be fetched, and the local tracking branch updated.
            This only works if we have a local tracking branch, which is the case
            if the remote repository had a master branch, or of the 'branch' option
            was specified for this submodule and the branch existed remotely
        :param progress: UpdateProgress instance or None if no progress should be shown
        :param dry_run: if True, the operation will only be simulated, but not performed.
            All performed operations are read - only
        :param force:
            If True, we may reset heads even if the repository in question is dirty. Additinoally we will be allowed
            to set a tracking branch which is ahead of its remote branch back into the past or the location of the
            remote branch. This will essentially 'forget' commits.
            If False, local tracking branches that are in the future of their respective remote branches will simply
            not be moved.
        :param keep_going: if True, we will ignore but log all errors, and keep going recursively.
            Unless dry_run is set as well, keep_going could cause subsequent / inherited errors you wouldn't see
            otherwise.
            In conjunction with dry_run, it can be useful to anticipate all errors when updating submodules
        :param env: Optional dictionary containing the desired environment variables.
            Note: Provided variables will be used to update the execution
            environment for `git`. If some variable is not specified in `env`
            and is defined in `os.environ`, value from `os.environ` will be used.
            If you want to unset some variable, consider providing empty string
            as its value.
        :param clone_multi_options:  list of Clone options. Please see ``git.repo.base.Repo.clone``
            for details. Only take effect with `init` option.
        :param allow_unsafe_protocols: Allow unsafe protocols to be used, like ext
        :param allow_unsafe_options: Allow unsafe options to be used, like --upload-pack
        :note: does nothing in bare repositories
        :note: method is definitely not atomic if recurisve is True
        :return: self"""
        ...
    @unbare_repo
    def move(
        self, module_path: PathLike, configuration: bool = ..., module: bool = ...
    ) -> Submodule:
        """Move the submodule to a another module path. This involves physically moving
        the repository at our current path, changing the configuration, as well as
        adjusting our index entry accordingly.

        :param module_path: the path to which to move our module in the parent repostory's working tree,
            given as repository - relative or absolute path. Intermediate directories will be created
            accordingly. If the path already exists, it must be empty.
            Trailing(back)slashes are removed automatically
        :param configuration: if True, the configuration will be adjusted to let
            the submodule point to the given path.
        :param module: if True, the repository managed by this submodule
            will be moved as well. If False, we don't move the submodule's checkout, which may leave
            the parent repository in an inconsistent state.
        :return: self
        :raise ValueError: if the module path existed and was not empty, or was a file
        :note: Currently the method is not atomic, and it could leave the repository
            in an inconsistent state if a sub - step fails for some reason
        """
        ...
    @unbare_repo
    def remove(
        self,
        module: bool = ...,
        force: bool = ...,
        configuration: bool = ...,
        dry_run: bool = ...,
    ) -> Submodule:
        """Remove this submodule from the repository. This will remove our entry
        from the .gitmodules file and the entry in the .git / config file.

        :param module: If True, the module checkout we point to will be deleted
            as well. If the module is currently on a commit which is not part
            of any branch in the remote, if the currently checked out branch
            working tree, or untracked files,
            is ahead of its tracking branch, if you have modifications in the
            In case the removal of the repository fails for these reasons, the
            submodule status will not have been altered.
            If this submodule has child - modules on its own, these will be deleted
            prior to touching the own module.
        :param force: Enforces the deletion of the module even though it contains
            modifications. This basically enforces a brute - force file system based
            deletion.
        :param configuration: if True, the submodule is deleted from the configuration,
            otherwise it isn't. Although this should be enabled most of the times,
            this flag enables you to safely delete the repository of your submodule.
        :param dry_run: if True, we will not actually do anything, but throw the errors
            we would usually throw
        :return: self
        :note: doesn't work in bare repositories
        :note: doesn't work atomically, as failure to remove any part of the submodule will leave
            an inconsistent state
        :raise InvalidGitRepositoryError: thrown if the repository cannot be deleted
        :raise OSError: if directories or files could not be removed"""
        ...
    def set_parent_commit(
        self, commit: Union[Commit_ish, None], check: bool = ...
    ) -> Submodule:
        """Set this instance to use the given commit whose tree is supposed to
        contain the .gitmodules blob.

        :param commit:
            Commit'ish reference pointing at the root_tree, or None to always point to the
            most recent commit
        :param check:
            if True, relatively expensive checks will be performed to verify
            validity of the submodule.
        :raise ValueError: if the commit's tree didn't contain the .gitmodules blob.
        :raise ValueError:
            if the parent commit didn't store this submodule under the current path
        :return: self"""
        ...
    @unbare_repo
    def config_writer(
        self, index: Union[IndexFile, None] = ..., write: bool = ...
    ) -> SectionConstraint[SubmoduleConfigParser]:
        """:return: a config writer instance allowing you to read and write the data
            belonging to this submodule into the .gitmodules file.

        :param index: if not None, an IndexFile instance which should be written.
            defaults to the index of the Submodule's parent repository.
        :param write: if True, the index will be written each time a configuration
            value changes.
        :note: the parameters allow for a more efficient writing of the index,
            as you can pass in a modified index on your own, prevent automatic writing,
            and write yourself once the whole operation is complete
        :raise ValueError: if trying to get a writer on a parent_commit which does not
            match the current head commit
        :raise IOError: If the .gitmodules file/blob could not be read"""
        ...
    @unbare_repo
    def rename(self, new_name: str) -> Submodule:
        """Rename this submodule
        :note: This method takes care of renaming the submodule in various places, such as

            * $parent_git_dir / config
            * $working_tree_dir / .gitmodules
            * (git >= v1.8.0: move submodule repository to new name)

        As .gitmodules will be changed, you would need to make a commit afterwards. The changed .gitmodules file
        will already be added to the index

        :return: this submodule instance
        """
        ...
    @unbare_repo
    def module(self) -> Repo:
        """:return: Repo instance initialized from the repository at our submodule path
        :raise InvalidGitRepositoryError: if a repository was not available. This could
            also mean that it was not yet initialized"""
        ...
    def module_exists(self) -> bool:
        """:return: True if our module exists and is a valid git repository. See module() method"""
        ...
    def exists(self) -> bool:
        """
        :return: True if the submodule exists, False otherwise. Please note that
            a submodule may exist ( in the .gitmodules file) even though its module
            doesn't exist on disk"""
        ...
    @property
    def branch(self) -> Head:
        """:return: The branch instance that we are to checkout
        :raise InvalidGitRepositoryError: if our module is not yet checked out"""
        ...
    @property
    def branch_path(self) -> PathLike:
        """
        :return: full(relative) path as string to the branch we would checkout
            from the remote and track"""
        ...
    @property
    def branch_name(self) -> str:
        """:return: the name of the branch, which is the shortest possible branch name"""
        ...
    @property
    def url(self) -> str:
        """:return: The url to the repository which our module - repository refers to"""
        ...
    @property
    def parent_commit(self) -> Commit_ish:
        """:return: Commit instance with the tree containing the .gitmodules file
        :note: will always point to the current head's commit if it was not set explicitly
        """
        ...
    @property
    def name(self) -> str:
        """:return: The name of this submodule. It is used to identify it within the
            .gitmodules file.
        :note: by default, the name is the path at which to find the submodule, but
            in git - python it should be a unique identifier similar to the identifiers
            used for remotes, which allows to change the path of the submodule
            easily
        """
        ...
    def config_reader(self) -> SectionConstraint[SubmoduleConfigParser]:
        """
        :return: ConfigReader instance which allows you to qurey the configuration values
            of this submodule, as provided by the .gitmodules file
        :note: The config reader will actually read the data directly from the repository
            and thus does not need nor care about your working tree.
        :note: Should be cached by the caller and only kept as long as needed
        :raise IOError: If the .gitmodules file/blob could not be read"""
        ...
    def children(self) -> IterableList[Submodule]:
        """
        :return: IterableList(Submodule, ...) an iterable list of submodules instances
            which are children of this submodule or 0 if the submodule is not checked out
        """
        ...
    @classmethod
    def iter_items(
        cls,
        repo: Repo,
        parent_commit: Union[Commit_ish, str] = ...,
        *Args: Any,
        **kwargs: Any
    ) -> Iterator[Submodule]:
        """:return: iterator yielding Submodule instances available in the given repository"""
        ...