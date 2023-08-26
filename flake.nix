{
  description = "A bible used on cli and on fortune.";


  outputs = { self, nixpkgs }:
    let

      lastModifiedDate = self.lastModifiedDate or self.lastModified or "19700101";
      # Generate a user-friendly version number.
      version = builtins.substring 0 8 lastModifiedDate;

      # System types to support.
      supportedSystems = [ "x86_64-linux" ];

      # Helper function to generate an attrset '{ x86_64-linux = f "x86_64-linux"; ... }'.
      forAllSystems = nixpkgs.lib.genAttrs supportedSystems;

      # Nixpkgs instantiated for supported system types.
      nixpkgsFor = forAllSystems (system: import nixpkgs { inherit system; overlays = [ self.overlay ]; });

    in

    {
      # A Nixpkgs overlay.
      overlay = final: prev: {

        avabible = with final; stdenv.mkDerivation rec {
          pname = "ava-bible-1.1";
          inherit version;

          src = ./.;

          buildInputs = [ pkgs.fortune ];

          preConfigure = ''
              cd blb
              export DESTDIR=$out
          '';

          makeFlags = [ "CC:=$(CC)" ];
        };
      };

      packages = forAllSystems (system:
        {
          inherit (nixpkgsFor.${system}) avabible;
        });

      # The default package for 'nix build'. This makes sense if the
      # flake provides only one package or there is a clear "main"
      # package.
      defaultPackage = forAllSystems (system: self.packages.${system}.avabible);
    };

}
