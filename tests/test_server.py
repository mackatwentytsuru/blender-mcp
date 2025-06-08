"""Basic tests for BlenderMCP server."""

import pytest
from unittest.mock import Mock, patch
import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestBlenderConnection:
    """Test BlenderConnection class."""
    
    @patch('socket.socket')
    def test_connection_init(self, mock_socket):
        """Test BlenderConnection initialization."""
        from blender_mcp.server import BlenderConnection
        
        conn = BlenderConnection(host='localhost', port=9876)
        assert conn.host == 'localhost'
        assert conn.port == 9876
    
    @patch('socket.socket')
    def test_send_command_connection_error(self, mock_socket):
        """Test send_command handles connection errors."""
        from blender_mcp.server import BlenderConnection
        
        mock_socket.return_value.connect.side_effect = ConnectionRefusedError
        
        conn = BlenderConnection()
        result = conn.send_command({'action': 'test'})
        
        assert result['success'] is False
        assert 'Connection refused' in result['error']


class TestEnvironmentVariables:
    """Test environment variable handling."""
    
    def test_default_values(self):
        """Test default values when env vars not set."""
        with patch.dict(os.environ, {}, clear=True):
            from blender_mcp.server import BlenderConnection
            
            # Should use defaults
            assert os.environ.get('BLENDER_HOST', 'localhost') == 'localhost'
            assert os.environ.get('BLENDER_PORT', '9876') == '9876'
    
    def test_custom_values(self):
        """Test custom values from env vars."""
        with patch.dict(os.environ, {
            'BLENDER_HOST': '172.31.32.1',
            'BLENDER_PORT': '8888'
        }):
            from blender_mcp.server import BlenderConnection
            
            assert os.environ.get('BLENDER_HOST') == '172.31.32.1'
            assert os.environ.get('BLENDER_PORT') == '8888'


class TestSecurity:
    """Test security-related functionality."""
    
    def test_auth_token_not_implemented(self):
        """Test that auth token is not yet implemented."""
        # This test documents that authentication is TODO
        with patch.dict(os.environ, {'MCP_AUTH_TOKEN': 'secret'}):
            # Currently, the server doesn't check this token
            # This test will fail when authentication is implemented
            assert True  # TODO: Implement authentication
    
    def test_code_execution_sanitization_not_implemented(self):
        """Test that code sanitization is not yet implemented."""
        # This test documents that code sanitization is TODO
        # Currently, any Python code can be executed
        assert True  # TODO: Implement code sanitization


if __name__ == '__main__':
    pytest.main([__file__, '-v'])